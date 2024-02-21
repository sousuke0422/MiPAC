# Change Log

## v0.6.1

[compare changes](https://github.com/yupix/MiPAC/compare/0.6.0...v0.6.1)

### 🚀 Enhancements

- FollowActionsをClientと分けた ([dc00a0e](https://github.com/yupix/MiPAC/commit/dc00a0e))
- Notes/search をサポート ([f3d04fb](https://github.com/yupix/MiPAC/commit/f3d04fb))

### 🏡 Chore

- FollowManagerでActionを再生成しないように ([bb93d03](https://github.com/yupix/MiPAC/commit/bb93d03))
- FollowActions.add メソッドを非推奨に、代わりにcreateメソッドを追加 ([69c89a7](https://github.com/yupix/MiPAC/commit/69c89a7))
- FollowActions.remove メソッドを非推奨に、代わりにdeleteメソッドを追加 ([df2ba4f](https://github.com/yupix/MiPAC/commit/df2ba4f))
- サポート状況を更新 ([be5e608](https://github.com/yupix/MiPAC/commit/be5e608))

### ❤️ Contributors

- Yupix ([@yupix](http://github.com/yupix))

## [Unreleased]

## [0.6.0] 2023-02-20

### Breaking changes 💔

#### AuthClient が削除されました

今まで MiAuth やアプリ作成方式でのアクセストークンを取得する際に使用できていた `AuthClient` を削除しました。今後は `MiAuth` クラスをご利用ください。

#### 以下のクラスを削除しました

この変更は Misskey の Schema に似せた形で再実装するにあたり、Misskey の Schema よりも細かくモデルを作成していたため、そういったものを削除した形となります。

- `UserDetailed` -> `UserDetailedNotMe | MeDetailed`
- `MeDetailedModerator` -> `MeDetailed`
- `UserDetailedModerator` -> `UserDetailedNotMe | MeDetailed`
- `UserDetailedNotLogined` -> `UserDetailedNotMe | MeDetailed`
- `AdminAnnouncementClientActions` -> `ClientAdminAnnouncementActions`
- `AnnouncementSystem` -> `AnnoucementDetailed`
- `MeRole` -> `RoleUser`

#### クラス名の変更

- `AdminAdvertisingModelActions` -> `ClientAdminAdActions`
- `AdminAdvertisingActions` -> `AdminAdActions`
- `AdminAdvertisingModelManager` -> `ClientAdminAdManager`
- `AdminAdvertisingManager` -> `AdminAdManager`
- `MutedUser` -> `Muting`

#### 引数に関する変更

`*Actions` 系にて `*_id` のような引数はすべてキーワード引数に変更されました。これはリスコフの置換法則に則るうえで必要な作業であり、今後のコード変更に対する耐性を上げるためでもあります。ご迷惑をお掛けしますがご理解のほどよろしくお願いいたします。

#### 戻り値の変更

- `Announcement.action -> ClientAdminAnnouncementActions` -> `Announcement.action -> ClientAdminAnnouncementManager`
- `AnnouncementDetailed.action -> ClientAdminAnnouncementActions` -> `AnnouncementDetailed.action -> ClientAdminAnnouncementManager`

#### `get_all` 引数を廃止

今まで多くの配列を返すメソッドをジェネレータとして作成していましたが、少ししかデータは要らないのに `async for` を書くのは大変ということで `get_all` 引数を廃止します。

これにより今まで `get_all` 引数があった ジェネレータは全て通常の list 等を返すメソッドに変更されます。
今まで通りのジェネレータとしての機能が必要な場合は `get_all_*` というメソッドが新しく増えているためそちらをご利用ください。

## [0.5.99] 2023-12-03

このリリースは最新の Misskey 向けに最適化された `develop` ブランチの物となります。インスタンスで `v11` や `v12` を利用している場合は更新しないことをおすすめします。

### Breaking changes 💔

#### v13 に合わせてメソッドやモデルを整理しました

主に削除されたモデルはチャットです。その他にも `admin` 向けのエンドポイントで既に削除されている物を削除しました。
v13 でのリクエストボディーに合わせて引数の追加なども行っています。

#### pypi からダウンロードできる MiPAC は最新の Misskey のみをサポートするようになります。

詳しくは[こちらの Issue](https://github.com/yupix/MiPAC/issues/94)を御覧ください。
今まで通りの全てのバージョンをサポートした MiPAC を利用したい場合は以下のコマンドで `shared` ブランチの物をご利用いただけます。

今後 `v11` や `v12` のブランチを作成しそれぞれの最新のバージョンをサポートする予定です。そのため、`shared` ブランチは保守モードに入り、基本的にはバグの修正のみを提供します。機能追加も行う可能性はありますが、v11 や v12、最新の Misskey のサポートが終わってからになります。

```bash
pip install git+https://github.com/yupix/Mi.py.git@shared
```

#### `Lite*` から始まるモデルの名前が `Partial*` に変更されます。

今まで Lite と Partial が混在していましたが、今回のアップデートを期に `Partial` に統一されます

### メソッドの変更

| v0.5.0                           | v0.6.0                               |
| -------------------------------- | ------------------------------------ |
| `ClientNoteActions.get_children` | `ClientNoteActions.get_all_children` |
| `ClientNoteActions.get_reaction` | `ClientNoteActions.get_reactions`    |

### Drive 周りの作り直し

Drive に関する Manager や Actions を全て作り直しました。詳細に記述してるといつまでも終わらないので、ご迷惑をおかけしますが、確認していただけると幸いです 🙏

### モデルの変更

一部のモデルがより良い形で再実装されました。結果的にモデル名が変わっています。以下がその変更後の表になります。

| v0.5.0      | v0.6.0      | 変更理由                                                                           |
| ----------- | ----------- | ---------------------------------------------------------------------------------- |
| UserRole    | PartialRole | Role と共通していた為 User よりも Role の Partial クラスにする方が適切だと考えた為 |
| PartialNote | Note        | 分ける必要性が無かったため(実際どこにも使用していなかった)                         |
| MuteUser    | MutedUser   | より分かりやすい名前に変更                                                         |

### 非推奨になったモデル/クラス

| 名前     | 削除されるバージョン | 理由               |
| -------- | -------------------- | ------------------ |
| UserRole | 0.7.0                | PartialRole に変更 |

### Other notable changes 📜

- `mipac.util` モジュールが削除されました
- 例外 `CredentialsError` が追加されました

## [0.5.1] 2023-10-03

### New Features ✨

#### `MeDetailed` モデルが追加され、自身に関する情報より多く扱えるようになりました

今後は API を使用した際に自動でユーザーが自分自身かを判断し、自身であった場合は `UserDetailed` ではなく、 `MeDetailed` を返すようになります。
`MeDetailed` と `UserDetailed` の共有体型の場合は `isinstance` を用いて判断が行えます。
また、`RoleUser` 等のように専用のユーザーモデルがある場合は `MeRole` のようなモデルを作成し、どちらかを返すようになります。

※まだ全てのメソッドに適応されたわけではなく、ごく一部のみの適応となっています。

```py
async def main():
    async with Client("https://nr.akarinext.org", "token") as client:
        api = client.api
        users = await api.admin.action.show_users(username="yupix")
        for user in users:
            if isinstance(user, MeDetailed):
                print(user.is_admin)
```

- `LiteUser` モデルに `badge_roles` プロパティーが追加されました

#### 以下のエンドポイントがサポートされました

| エンドポント               | MiPAC でのメソッド                        |
| -------------------------- | ----------------------------------------- |
| `/api/admin/invite/create` | `api.admin.invite.action.create_invite`   |
| `/api/admin/invite/list`   | `api.admin.invite.action.get_invite_list` |
| `/api/roles/list`          | `api.role.action.get_list`                |
| `/api/roles/show`          | `api.role.action.get`                     |
| `/api/roles/users`         | `api.role.action.get_users`               |
| `/api/roles/notes`         | `api.role.action.get_notes`               |

### Fixed 🛠️

- `RoleUser` モデルで `LiteUser` を使用していましたが、正しくは `UserDetailed`

### 依存関係の更新 📦

- `aiohttp`: `3.8.4` => `3.8.5`

#### 貢献者向け情報

##### `axblack` を使ったフォーマットを辞めました

理由としては `axblack` の更新が止まっており、また移行先である `blue` も更新が止まっているからです。今後は 通常の `black` を使用したフォーマット使用するようにお願いします。

##### Model には `AbstractModel` を継承してください

`pagination_iterator` 関数が新規に追加され、pagination の処理を楽に使えるようになりました。その際に Model 以外のクラスを受け取らないよう識別するのに使用します。

## [0.5.0] 2023-07-26

### New Features ✨

#### `Client` で `async with` 構文がサポートされました

一時的にセッションを作成したい場合などに `login` メソッドや `close_session` メソッドを使用するのは非常に手間であるため、一時的にセッションを作成したいといった場合におすすめします。

```py
async with Client('server url', 'token') as client:
    api = client.api
    async for emoji in api.admin.emoji.action.gets():
        print(emoji)
```

#### 一意の ID を持つモデルで比較演算がサポートされました

サポートされた演算は `__eq__` と `__ne__` の 2 つです。一意の ID と判断しにくい物は現状サポートしていません。
一意の ID があるにもかかわらず、サポートされていないモデルがある際は Issue を作成してください。

```py
note_one = await api.note.action.get('note one')
note_two = await api.note.action.get('note one')
note_three = await api.note.action.get('note two')
print(note_one == note_two, note_one != note_two)
print(note_one == note_three, note_one != note_three)
```

#### File モデルに `api` プロパティーが追加されました

今まではモデルに `api` プロパティーが無かったため、 `api` プロパティーからアクションにアクセスし、対象のメソッドに対してファイル ID などといった引数を自分で渡す必要がありましたが、今後はモデルから直接実行できます。

```diff
-async for file in api.drive.file.action.get_files(get_all=True):
-  await api.drive.file.action.remove(file.id)
+async for file in api.drive.file.action.get_files(get_all=True):
+  await file.api.action.remove()
```

#### `FileActions` に `save` メソッドが追加されました

指定したパス、または Buffer にファイルをダウンロードできるようになりました。
パスを指定する場合

```py
async for file in api.drive.file.action.get_files(get_all=True):
    await file.api.action.save(f'./test/{file.name}')
```

Buffer を指定する場合:

```py
async for file in api.drive.file.action.get_files(get_all=True):
    with open(f'./test/{file.name}', mode='mb') as f:
      await file.api.action.save(f)
```

#### 以下のエンドポイントがサポートされました

- `/api/admin/emoji/set-license-bulk`
- `/api/antennas/create`
- `/api/antennas/delete`
- `/api/antennas/list`
- `/api/antennas/notes`
- `/api/antennas/show`
- `/api/antennas/update`
- `/api/clips/create`
- `/api/clips/delete`
- `/api/clips/list`
- `/api/clips/show`
- `/api/clips/update`
- `/api/notes/clips`
- `/api/clips/add-note`
- `/api/clips/remove-note`
- `/api/clips/notes`
- `/api/clips/my-favorites`
- `/api/users/clips`
- `/api/channels/create`
- `/api/channels/featured`
- `/api/channels/follow`
- `/api/channels/followed`
- `/api/channels/owned`
- `/api/channels/show`
- `/api/channels/unfollow`
- `/api/channels/update`
- `/api/channels/favorite`
- `/api/channels/unfavorite`
- `/api/channels/my-favorites`
- `/api/channels/search`

### Breaking changes 💔

#### 全取得の際の引数 `all` が `get_all` に変更されます。

影響を受けるのはキーワード引数を使用していた方です。位置引数を使用していた方は特に問題ありません。

```diff
-Client.api.admin.emoji.action.gets(all=True)
+Client.api.admin.emoji.action.gets(get_all=True)
```

#### `NoteManager.get` メソッドが削除されました

何故あったのか分かりませんが、Manager の責務から逸脱しているためです

#### NoteActions に関する変更

- `NoteActions.get` `NoteActions.fetch` メソッドにおいて `note_id` が optional になっているのはおかしいため必須の引数に変更しました

### Fixed 🛠️

- 一部 `all` 引数が存在しないが、 built-in の `all` が存在することで動作していた箇所が修正されました
- `ClientNoteActions` において `note_id` が無かった場合の例外処理が無かった為追加

### Other notable changes 📜

- 新しい実績をサポートしました
- クリップがサポートされました
- ロールの作成時に `is_explorable` を使用できるようになりました。
  - 最新のインスタンス等で無いと使用できない可能性があります
- update_meta のリクエスト時に `server_rules` パラメータが使用できるようになりました
  - このパラメータは `13.11.3` 以降のバージョン（`13.11.3`は含みません）を使用している場合は必須であり、それ以前のバージョンを使用している場合は指定するとエラーが発生する可能性があります。
- `NoteActions.get_replies` が `ClientNoteActions.getriplies` に移動され、 `ClientNoteActions` でも使用可能になりました。（NoteActions は ClientNoteActions を継承しているため今後とも使用できます）
- 全取得が以下のメソッドでサポートされました。それに伴い、一部のメソッドがジェネレーターになっています。
  - `FederationActions.get_followers`
  - `FederationActions.get_following`
  - `FederationActions.get_users`
  - `AdminAnnouncementActions.gets`
  - `AdminRoleModelActions.get_users`
  - `AdminAdvertisingActions.get_list`
  - `AdminActions.get_moderation_logs`
  - `NoteActions.get_replies`
  - `NoteActions.gets`
  - `FileActions.get_files`
  - `ClientFolderActions.get_files`
  - `DriveActions.get_folders`
- `Pagination` クラスが追加されました
  - 基本的にユーザーが使うことは想定されていません
- [@omg-xtao](https://github.com/omg-xtao) can cancel setup_logging when init client.
- models/user にあった `FollowRequest` クラスが削除されました

## [0.4.3] 2023-04-25

### Added

- 以下のエンドポイントがサポートされます。
  - `emoji`
  - `channels/favorite`
  - `channels/unfavorite`
  - `channels/my-favorites`
- 以下のクラスを追加
  - `IChannelNote`
  - `PartialNote`
- `Note` クラスで `tags` を取得できるように
- `Client` クラスのコンストラクタ引数に以下を追加
  - `use_version`
  - `use_version_autodetect`
- `ClientManager` に属性　`emoji` を追加
- `Channel` に `api` プロパティを追加
- `CustomEmoji` に `host` プロパティを追加
- `ChannelLite` に `api` プロパティを追加
- `Folder` に `api` プロパティを追加
- `File` に `api` プロパティを追加
  - `Channel` クラスは `ChannelLite` を継承しているため必然的にこちらにも `api` プロパティが増えています

### Changed

- `FileActions` の `remove_file` メソッドが非推奨になります。 今後は `remove` メソッドをご利用ください。
- `v0.5.0`で削除されます。
- `INoteRequired` が `IPartialNote` に変更されました
- `mipac.util` モジュールは `mipac.utils` 配下の `auth`, `cache`, `format`, `log`, `util`の 5 つに分離しました。そのため `v0.5.0`で削除されます。
  - 今後は `mipac.utils.*` をご利用ください

### Fixed

- `FileActions` クラスの `show_file` メソッドで引数にデフォルト値が入っていないのを修正
- `Note` のプロパティで一部戻り値が正しくない
- `ChannelLite` クラスに `is_following` プロパティは存在してはいけないので修正
  - tip: `Channel` クラスに移動されました

### Removed

- `LiteUser` から `name` プロパティが削除されました。
  - 今後は `nickname` をご利用ください

## [0.4.2] 2023-03-22

### Added

#### `config.features` が追加されました

MiPAC は v13, v12, v11 という大きな区切りでエンドポイントが利用可能かを確認しています。その都合上、v13 でサポートされいた物、例えばチャットが`13.7.0`で廃止されたような場合、MiPAC は最新の Misskey に追従しているため、デフォルトの挙動を変更します。これにより、`13.7.0`に更新してなかったり、`fork`を使用していてチャットが存在する場合でもチャットを使用すると例外である`NotSupportVersion`が発生してしまいます。その対策としてこの機能が追加されました。
この config の主な役割は以下の通りです。

- 最新の Misskey では使用できないが、自身が使用しているサーバーのバージョンでは使用できる場合に該当する物を有効にすることで例外を返さず、使用できるようにする

使い方は以下の通りです。また、現在サポートされている feature は`chat`のみです。

```py
async def main():
    client = Client(auth.currentUser.url, auth.currentUser.token)
    await client.http.login()
    api = client.api
    client.config.from_dict(features={'chat': True})
```

#### `config.limits` が追加されました

MiPAC では文字数等にデフォルトで最新の Misskey の値を入れています。しかし、一部の Fork で文字数の制限が緩和されている・制限されている場合に正しくエラーを返せなくなる可能性があります。その対策としてこの機能が追加されました。

また、自分で作成・使用している Fork でこれ存在するからデフォルトでサポートしてくれない？という物がありましたら、Issue を作成してくだされば検討します。

- Note 周りのメソッドで`visibility`の型を正確に
- 以下のエンドポイントがサポートされます。
  - `i/claim-achievement`
  - `blocking/create`
  - `blocking/delete`
  - `blocking/list`
  - `admin/ad/create`
  - `admin/ad/delete`
  - `admin/ad/list`
  - `admin/ad/update`
- Added `IT_ACHIEVEMENT_NAME` fixed variable.
- Added class the given below.
  - Channel
    - `IChannelLite`
    - `ChannelLite`
    - `ChannelActions`
    - `ChannelManager`
  - Blocking
    - `BlockingUser`
    - `IBlockingUser`
    - `BlockingActions`
    - `BlockingManager`
  - Ad
    - `AdminAdvertisingModelActions`
    - `AdminAdvertisingActions`
    - `Ad`
    - `IAd`
    - `AdminAdvertisingModelManager`
    - `AdminAdvertisingManager`
- Added `block` attribute to `UserManager`.
- Added `channel` attribute to `ClientManager`.
- Added `reaction_emojis` property to `Note`.
- Added `reaction_acceptance` property to `Note`.

### Changed

- chat が v13 で廃止された為 v13 を利用している際は例外を返すように変更しました。
  - v13 だが、fork や chat が廃止される前のバージョンを使用していてチャットが使用したい際は新しい機能である `config.features` をご利用ください
- aiohttp のバージョンを `3.8.4`に固定
- Token を使用しなくても API が一部使用できるようになりました。当然ですが、認証が必要な API を使用した場合はエラーが出ます。
- `Config.from_dict` の引数が全てキーワード引数になりました。これは今後 Config に引数が増えた際など、変更に強くするためです。

### Removed

- サポートする気が無いため、sphinx を用いたドキュメントを削除

### Fixed

- `Note.reply`のキーが`renote`になっていて取得不可になっていた

## [0.4.1] 2023-03-14

### Added

#### バージョンの自動検出機能が追加されました（β）

これはデフォルトで有効になっており、有効の間は自動的に `/api/meta` からバージョンを推論します。機能としては以下の通りです

- 11, 12, 13 にヒットした場合それらにバージョンを変更する - ヒットしなかった場合は何もしない
  Misskey 公式のバージョンニングを元に判断している為、独自のバージョニングを行っているフォーク等では正常に動作しない可能性があります。その際は `client.config.use_version_autodetect = False` とすることで無効にすることが可能です。また、手動でバージョンを設定する場合も off にしてください。
  一部の API はバージョンとフォークの種類で判断しています。そのため公式のバージョン的には使用できないが、フォークの機能として存在するという場合は報告をくださればサポートします。

- Added `role` property to `AdminManager`.
- Added `remove_none` argument to request method.
- Added method to`ClientActions` class the given below.
  - `get_announcements`
- Added class the given below.
  - `AdminUserActions`
  - `AnnouncementCommon`
  - `Announcement`
  - `AnnouncementSystem`
  - `IMetaAnnouncement`
  - `IAnnouncementSystem`
  - `AdminAnnouncementClientActions`
  - `AdminAnnouncementActions`
  - `AdminAnnouncementManager`
  - `IModerationLog`
  - `ModerationLog`
  - `ServerInfoCpu`
  - `ServerInfoMem`
  - `ServerInfoFs`
  - `ServerInfoNet`
  - `ServerInfo`
  - `IServerInfoCpu`
  - `IServerInfoMem`
  - `IServerInfoFs`
  - `IServerInfoNet`
  - `IServerInfo`
  - `ITableStats`
  - `IIndexStat`
  - `IndexStat`
  - `IUserIP`
  - `UserIP`
  - `FederationActions`
  - `FederationManager`
  - `IFederationInstanceStat`
  - `IFederationFollowCommon`
  - `IFederationFollower`
  - `IFederationFollowing`
- Roles
  - `IRolePolicieValue`
  - `IRolePolicies`
  - `IRole`
  - `RolePolicyValue`
  - `RolePolicies`
  - `Role`
  - `AdminRoleActions`
  - `AdminRolesManager`
  - `IRoleUser`
  - `RoleUser`
- Achievements
  - added `IAchievementNf` class.
  - added `NotificationAchievement` class.
  - added `Achievement` class.
  - added `get_achievements` method at `UserActions` class.
  - added `achievements` property at `UserDetailed` class.
- Note
  - content field auto convert empty string to None

### Changed

- Maximum number of characters has been changed from 79 to 99
  - The main reason for this change is to solve the problem that the MiPAC code is inevitably longer because of the method chain. We have kept it to the maximum of [pep8](https://peps.python.org/pep-0008/#maximum-line-length).
- Changed a method that was returning an `AsyncIterator` to return an `AsyncGenerator`.
  - Generator is more correct than Iterator because it is the correct usage.
- Changed class name the given below.
  - `IAnnouncement` -> `IMetaAnnouncement`
- `cache` decorator no longer uses `dynamic_args` decorator

### Removed

- Delete `dynamic_args` decorator.
- Delete debug log.

## [0.4.0] 2023-01-18

### Added

- added DocString.
- added `get_state` method at `ClientNoteActions` class.
- added `INoteState` class.
- added `NoteState` class.
- added `IBasePoll` class.
- added `ICreatePoll` class.
- added `MiPoll` class.
- added `PollManager` class.
- added `PollActions` class.
- added `AdminEmojiActions` class.
- added `AdminManager` class.
- added `AdminModeratorManager` class.
- added `ActiveUsersChart` class.
- added `IDriveChart` class.
- added `IDriveLocalChart` class.
- added `IDriveRemoteChart` class.
- added attribute `is_official` at `Config` class.
  - became `is_ayuskey` attribute is deprecated(I'll remove with v0.4.0)
- added `get_exception_from_id` function.
- Return an exception appropriate for the error encountered.
- [@omg-xtao](https://github.com/omg-xtao) added `users_search_by_username_and_host` method at `UserActions` class [#24](https://github.com/yupix/MiPAC/pull/24).
- [@omg-xtao](https://github.com/omg-xtao) added `note_translate` method at `UserActions` class [#24](https://github.com/yupix/MiPAC/pull/24).
- [@omg-xtao](https://github.com/omg-xtao) added `users_search` method at `UserActions` class [#24](https://github.com/yupix/MiPAC/pull/24).
- added new `ClientActions` class.
- added `avatar_color` property at `LiteUser` class.
  - Note: Since avatar_color is deprecated in v13, only None is returned for v13 instances.
- added `un_renote` method at `ClientNoteActions` class.
- added `get_children` method at `ClientNoteActions` class.
- added `invalidate` method at `FollowActions` class.
- added `cancel` method at `FollowRequestActions` class.
- added `mute` attribute at `UserManager` class.
- added `MuteManager` class.
- added `MuteActions` class.
- added `MuteUser` class.
- added `IMuteUser` class.
- added `AdminActions` class.
- added `ICustomEmojiLiteRequired` class.
- The following methods are added to the `AdminEmojiActions` class.
  - `gets`
  - `gets_remote`
- added some meta class.
  - `ICPU`
  - `IPolicies`
  - `IAnnouncement`
  - `IV12Features`
  - `IV11Features`
  - `IFeatures`
  - `IV12AdminMeta`
  - `ISharedAdminMeta`
  - `ILiteV12Meta`
  - `ILiteV11Meta`
  - `IMetaCommonV12`
  - `ICommonV11`
  - `IMetaCommon`
  - `ILiteMeta`
  - `IV12Meta`
  - `IMeta`
  - `IAdminMeta`
  - `Policies`
  - `Features`
  - `Meta`
  - `AdminMeta`
  - `CPU`
  - `MetaCommon`
  - `LiteMeta`
- added some federation class.
  - `IFederationInstanceRequired`
  - `IFederationInstance`
  - `FederationInstance`
- added some notification classes.
  - `Notification`
  - `NotificationFollow`
  - `NotificationFollowRequest`
  - `NotificationNote`
  - `NotificationPollEnd`
  - `NotificationReaction`
  - `IUserNf`
  - `INoteNf`
  - `IPollEndNf`

### Changed

- rename `ActiveUsersChartPayload` class to `IActiveUsersChart` class.
- rename `DriveLocalChartPayload` class to `IDriveLocalChart` class.
- rename `DriveRemoteChartPayload` class to `IDriveRemoteChart` .class.
- rename `DriveChartPayload` class to `IDriveChart` class.
- The attribute `emojis` for Note and LiteUser is obsolete in misskey v13, so v13 will return an empty list.
- config is now a global variable.
  - If you want to change the config, please use `Client.config.from_dict`.
- CustomEmoji now inherits PartialCustomEmoji.
- PartialCustomEmoji url has been changed to return `str | None` to match v13.
- AdminManager's `get_invite` method has been moved to `AdminActions.
- **BREAKING CHANGE** `ClientActions` has been changed to `ClientManager`
- **BREAKING CHANGE** Some paths will be changed as follows
  - `manager.admin` -> `manager.admins`
  - `manager.admin.manager` -> `manager.admins.admin`
  - `actions.admin` -> `actions.admins`
- **BREAKING CHANGE**
  - The `action` property in the model has been changed to `api`.
    - Change `note.action.send` to `note.api.action.send`.
  - Moved the reaction attribute of `ClientActions` to `NoteManager`.
    - Change `api.reaction` to `api.note.reaction`.
  - Moved methods from `AdminEmojiManager` to `AdminEmojiActions`.
    - Change `api.admin.emoji.add` to `api.admin.emoji.action.add`.
  - Moved methods from `AdminModeratorManager` to `AdminModeratorActions`.
    - Change `api.admin.moderator.add` to `api.admin.moderator.action.add`.
  - Moved methods from `ChartManager` to `ChartActions`.
    - Change `api.chart.get_active_user` to `api.chat.action.get_active_user`.
  - Moved methods from `FollowManager` to `FollowActions`.
    - Change `api.user.follow.add` to `api.user.follow.action.add`.
  - Moved methods from `FollowRequestManager` to `FollowRequestActions`.
    - `api.user.follow.action.get_all`.
  - Moved some attributes of `NoteActions` to `NoteManager`.
    - Change `api.note.action.reaction.add` to `api.note.reaction.action.add`.
  - Moved the reaction attribute of `NoteActions` to `ClientNoteManager`.
    - Change `api.note.action.reaction` to `api.note.reaction.action`.
    - Change `api.note.action.favorite` to `api.note.favorite.action`.

### Fixed

- can't delete emoji with v12.
- fixed `ChatMessage` model.
  - For v13, the url is automatically generated. (Although it returns None by type, it never actually returns None.
- fixed `Chat` action.
- fixed `Chat` action.

### Removed

- The following attributes have been removed `api.user.action.note`
- Delete `RawActiveUsersChart` class.
- Delete `RawDriveLocalChart` class.
- Delete `RawDriveRemoteChart` class.
- Delete `RawDriveChart` class.
- Delete `get_user` method at `FollowRequestActions` class.
- removed some meta classes.
  - `LiteInstanceMeta`
  - `IInstanceMetaLite`
  - `IInstanceFeatures`
  - `IInstancePolicies`
  - `InstanceMeta`

## [0.3.1] 2022-12-24

### Added

- added `NoteDeleted` class.
- added `INoteUpdatedDeleteBody` class.
- added `INoteUpdatedDelete` class.
- `str_to_datetime` 関数を追加

### Fixed

- `PartialReaction` クラスで `user_id` が取得できない
- `INoteUpdatedReaction` の型が間違っている

## [0.3.0] 2022-12-24

### Fixed

- fix `INoteUpdated` type

### Changed

- **BREAKING CHANGE** Required Python version is 3.11

## [0.2.8] 2022-12-23

### Added

- `LiteUser` に `action` プロパティを追加しました。
  - これにより `UserDetailed` の方から `action`が削除されていますが、`UserDetailed` は `LiteUser` を継承しているため今まで通りご利用いただけます
- `UserActions` クラスに `get_profile_link` メソッドを追加しました

## [0.2.7] 2022-12-23

### Fixed

- fix: TypedDict type error by [@omg-xtao](https://github.com/omg-xtao) in [#20](https://github.com/yupix/MiPAC/pull/20)

## [0.2.6] - 2022-12-08

### Added

- `INoteUpdated` クラスを追加しました
- `INoteUpdatedReactionBody` クラスを追加しました
- `INoteUpdatedReaction` クラスを追加しました
- `PartialCustomEmoji` クラスを追加しました
- `PartialReaction` クラスを追加しました

## [0.2.5] - 2022-12-08

### Added

- `ISignin` クラスを追加

### Fixed

- Note モデルの `content` が無い場合 KeyError になる
- Note モデルの `cw` が無い場合 KeyError になる

## [0.2.4] - 2022-12-08

### Added

- `ClientNoteManager` クラスを追加しました
- `ClientNoteActions` クラスを追加しました

### Changed

- `NoteActions` が持っているノートに対する操作を `ClientNoteActions` に移動しました
  - 継承しているため今まで通り使用できます

### Fixed

- send メソッドの引数 `extract_hashtags` が正常に動作しない

## [0.2.3] - 2022-11-27

### Fixed

- `NoteAction.send` メソッドで作成したノートのモデルが生成できない
- `request` メソッドで戻り値が list ではなく dist だった場合 snake case に置き換えできない

## [0.2.2] - 2022-11-27

### Added

- `LiteUser` に属性 `name` を互換性の為に再追加しましたが、非推奨です。v0.4.0 で削除する予定です
  - `username` と `name` の違いを区別しにくい可能性がある為、新たに使用する際は `nickname` を使用することを推奨しています

### Changed

- deprecated に関する仕組みを変更しました。
  - 該当するコードを表示するようになっています

### Fixed

- 型の間違い等
- 使用しているインポートが`TYPE_CHECKING`の条件式の中に入っていた為使用できない
- `get_mention` メソッドで`username` ではなく`nickname`を使用していた為正しい mention が作れない
- `LiteUser` クラスの属性`instance` で Bot と同じインスタンスのユーザーの場合は None を返せず KeyError になる可能性があった
- `LiteUser` クラスの属性 `host` を取得すると KeyError になる可能性があった

### Removed

- `deprecated_property` decorator を削除しました
- `deprecated_func` decorator を削除しました

## [0.2.1] - 2022-11-27

### Added

- `NoteActions` に `gets` メソッドが追加されました #MP-20
- Type Hint の追加

### Changed

- WebSocket を使用した際のレスポンスクラスを `MisskeyClientWebSocketResponse` クラス に
- `Reaction` クラスを `NotificationReaction` に変更しました
- `IUserLite` を `ILiteUser` に変更しました
- `LiteUser` の属性 `name` を `nickname` に変更しました。 `LiteUser` を継承しているクラスも同様に変更されていますのでご注意ください。

### Removed

- print を使用したデバッグログを削除しました

## [0.2.0] - 2022-11-02

### Added

- added `Modeler` class
- added `IReactionRequired` class
- added `IAds` class
- added `LiteInstance` class
- added `IReactionNf` class
- added `INote` class
- added `ICustomEmoji` class
- added `CustomEmoji` class
- added `InstanceMeta` class
- added `LiteInstanceMeta`
- added `IInstanceMetaLiteRequired` class
- added `IInstanceMetaLite` class
- added `IInstanceMeta` class
- added `IPage` class
- added `IPageRequired` class
- added `IUserDetailedField` class
- added `IUserDetailedRequired` class
- added `IUserDetailed` class
- added `ChatGroup` class
- added `ChatMessage` class
- added `IChatGroup` class
- NoteActions クラスに `get` `fetch` メソッドを追加
- データをキャッシュするためのツールを utils.py に追加
- orjson が使用者の環境にある場合は json ではなく orjson を使用するようになりました

### Changed

- `Dict[Any, Any]` のような構文を typing モジュールを使わない `dict[any, any]` に変更
- `List[Any, Any]` のような構文を typing モジュールを使わない `list[any, any]` に変更
- `Channel` クラスを `RawChannel` を用いて作るように
- `PinnedNote` クラスを `RawPinnedNote` を用いて作るように
- change class name `PinnedNotePayload` -> `IPinnedNote`
- change class name `ChannelPayload` -> `IChannel`
- change class name `NotePayload` -> `INote`
- **BREAKING CHANGE** renamed `Client.action` to `Client.api`.

### Removed

- `Renote` クラスを削除しました。今後は `Note` クラスをご利用ください
- `IRenote`, `RenotePayload` クラスを削除しました。今後は `INote` クラスをご利用ください
- `RawEmoji`, `Emoji` クラスを削除しました。 今後は `CustomEmoji` クラスをご利用ください
- `EmojiPayload` クラスを削除しました。今後は `ICustomEmoji` クラスをご利用ください
- `IReactionRequired`, `ReactionPayload`を削除しました。 今後は `IReactionNf` クラスをご利用ください
- `RawUser`, `User` クラスを削除しました。今後は `UserDetailed`, `LiteUser` クラスをご利用ください
- `RawInstance` クラスを削除しました。今後は `LiteInstance` クラスをご利用ください
- `RawProperties` クラスを削除しました。今後は `FileProperties` クラスをご利用ください
- `RawFolder` クラスを削除しました。今後は `Folder` クラスをご利用ください
- `RawFile` クラスを削除しました。 今後は `File` クラスをご利用ください
- `RawChat`, `Chat` クラスを削除しました。 今後は `ChatMessage` クラスをご利用ください
- `ChatPayload` クラスを削除しました。 今後は `IChatMessage` クラスをご利用ください
- `get_note` メソッドを削除しました。今後は `get` もしくは `fetch` メソッドをご利用ください
- `aiocache` を使用しないようになりました

### Fixed

- 一部の型が正しくないのを修正しました

## [0.1.0] - 2022-05-28

### Added

- `__all__` の定義
- utils.py に `AuthClient` クラスを追加しました
- `Config` クラスを追加しました
- `Client` クラスの引数に `config` を追加しました
- `FileActions` クラスを追加しました
- `FolderActions` クラスを追加しました
- README.md に使い方を追加

### Changed

- `Note` クラスの`created_at` 属性の type hint を `Optional[str]` => `Optional[datetime]` に変更
- `Note` クラスの `cw` 属性の取得方法が get ではなかったので修正
- **BREAKING CHANGE** `FileManager`, `FolderManager`, `DriveManager`の役割が変わりました
  - 例だと `FolderManager.get_files()` だったコードが `FolderManager.action.get_files()` と行ったふうに Actions クラスを経由するようになりました
- 開発者向け情報 `Folder` クラスの引数に `client` を追加しました

### Fixed

- config が無く動かなかった場所の修正
- 誤った型の修正

### Removed

- 重複した属性を削除
- 不要な import の削除
- 終わっている TODO を削除しました
